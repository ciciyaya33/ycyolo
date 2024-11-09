import os
from ultralytics import YOLOv10

# 创建 results 文件夹（如果不存在）
if not os.path.exists('results'):
    os.makedirs('results')

# 加载模型
model = YOLOv10("best.pt")

# 进行预测
results = model.predict("2022329600041-21.jpg")

# 显示结果
results[0].show()

# 保存结果到 results 文件夹
output_path = os.path.join('results', '2022329600041-21_result.jpg')
results[0].save(output_path)

print(f"Results saved to {output_path}")
