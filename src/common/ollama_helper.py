import subprocess
import re
from packaging import version

def get_installed_ollama_models():
    """获取本地已安装的Ollama模型列表"""
    try:
        result = subprocess.run(
            ['/usr/local/bin/ollama', 'list'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ollama命令执行失败: {e.stderr}") from e
    except FileNotFoundError:
        raise RuntimeError("未找到ollama命令，请确保已正确安装Ollama")

def parse_deepseek_versions(output):
    """解析版本号并过滤DeepSeek模型"""
    pattern = r"deepseek.*[:]?(?P<version>\d+[\.\d]*[b]?)"
    versions = []
    print(output)
    for line in output.split('\n'):
        if 'deepseek' in line.lower():
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                raw_version = match.group('version').lower().rstrip('b')
                print(raw_version)
                try:
                    # 转换版本号为语义化版本对象
                    ver = version.parse(raw_version)
                    versions.append((ver, line.strip().split()[0]))
                except version.InvalidVersion:
                    pass
    return versions

def get_optimal_deepseek():
    """获取最优DeepSeek版本"""
    try:
        output = get_installed_ollama_models()
        versions = parse_deepseek_versions(output)
        
        if not versions:
            raise ValueError("未检测到已安装的DeepSeek模型")
            
        # 按语义化版本排序
        sorted_versions = sorted(versions, key=lambda x: x, reverse=True)
        return sorted_versions[0][1]
        
    except Exception as e:
        print(f"错误: {str(e)}")
        return None
