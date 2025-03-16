import sys  
import os  
# 获取当前脚本的绝对路径的父目录（src/prompt 的上级目录 src）  
current_dir = os.path.dirname(os.path.abspath(__file__))  
parent_dir = os.path.dirname(current_dir)  
sys.path.append(parent_dir)  