from pathlib import Path
import os

class ProjectPaths:
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent
    
    @classmethod
    def get_project_path(cls, *paths) -> Path:
        """获取项目中的文件路径
        
        Args:
            *paths: 相对于项目根目录的路径部分
            
        Returns:
            完整的文件路径
        """
        return cls.ROOT_DIR.joinpath(*paths)
    
    @classmethod
    def ensure_dir(cls, *paths) -> Path:
        """确保目录存在，如果不存在则创建
        
        Args:
            *paths: 相对于项目根目录的路径部分
            
        Returns:
            目录路径
        """
        dir_path = cls.get_project_path(*paths)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path