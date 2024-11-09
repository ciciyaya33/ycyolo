from ultralytics import YOLOv10

model_yaml_path = "ultralytics/cfg/models/v10/yolov10n.yaml"
data_yaml_path = "/root/autodl-tmp/yolov10-main/data/data.yaml"
pre_model_name = "yolov10n.pt"

if __name__ == '__main__':
    model = YOLOv10(model_yaml_path).load(pre_model_name)
    results = model.train(data=data_yaml_path,epochs=200,batch=64,name='train_v10',device=0)