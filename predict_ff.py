from openvino.runtime import Core

# 初始化 OpenVINO Core 对象
core = Core()

# 读取 ONNX 模型
onnx_model_path = 'best.onnx'
model = core.read_model(model=onnx_model_path)

# 定义保存路径
xml_path = 'optimized_model.xml'
bin_path = 'optimized_model.bin'

# 保存为 IR 格式（.xml 和 .bin）
core.save_model(model, xml_path)

# 编译模型
compiled_model = core.compile_model(model=model, device_name='CPU')

print(f"模型已优化并保存为：{xml_path} 和 {bin_path}")
