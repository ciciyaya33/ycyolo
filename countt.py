import os

# 定义标注类别
categories = ['Header', 'Title', 'Text', 'Figure', 'Foot']

# 用于映射类别名称到标注文件中的ID
category_to_id = {category: i for i, category in enumerate(categories)}

def count_annotations(label_file):
    """
    统计单个标注文件中各类标注框的数量。
    假设标注文件格式为：class_id center_x center_y width height
    """
    counts = {category: 0 for category in categories}
    
    # 打开并读取标注文件
    with open(label_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                class_id = int(parts[0])  # 类别ID
                if class_id >= 0 and class_id < len(categories):
                    category = categories[class_id]
                    counts[category] += 1

    return counts

def process_directory(data_dir):
    """
    遍历数据集中的图片和标签文件夹，统计每个类别的标注框数量。
    """
    overall_counts = {category: 0 for category in categories}
    
    # 遍历各个子文件夹: test, train, valid
    for subdir in ['train', 'test', 'valid']:
        images_dir = os.path.join(data_dir, subdir, 'images')
        labels_dir = os.path.join(data_dir, subdir, 'labels')

        # 获取images和labels文件夹中的所有文件
        image_files = os.listdir(images_dir)
        for image_file in image_files:
            label_file = image_file.replace('.jpg', '.txt')  # 假设图片为jpg，标签文件为txt

            # 如果标签文件存在，进行统计
            label_path = os.path.join(labels_dir, label_file)
            if os.path.exists(label_path):
                counts = count_annotations(label_path)
                
                # 更新总统计信息
                for category, count in counts.items():
                    overall_counts[category] += count

    return overall_counts

def main():
    data_dir = 'data'  # data文件夹路径
    overall_counts = process_directory(data_dir)

    # 输出统计结果
    print("各类别标注框数量统计：")
    for category, count in overall_counts.items():
        print(f"{category}: {count}")

if __name__ == '__main__':
    main()
