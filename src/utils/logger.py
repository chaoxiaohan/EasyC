from loguru import logger
import sys
import os

# 创建日志目录
log_path = "logs"
if not os.path.exists(log_path):
    os.makedirs(log_path)

# 配置日志格式
fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} | {message}"

# 移除默认的控制台输出
logger.remove()

# 添加控制台输出
logger.add(
    sys.stdout,
    format=fmt,
    level="INFO",
    colorize=True
)

# 添加文件输出
logger.add(
    os.path.join(log_path, "app_{time:YYYY-MM-DD}.log"),
    format=fmt,
    level="DEBUG",
    rotation="00:00",
    retention="30 days",
    encoding="utf-8"
)

# 添加错误日志
logger.add(
    os.path.join(log_path, "error_{time:YYYY-MM-DD}.log"),
    format=fmt,
    level="ERROR",
    rotation="00:00",
    retention="30 days",
    encoding="utf-8"
)