""" Cut template data
"""
import os, shutil

# i/o paths
mess_dir = '/home/zhouyj/software/MESS'
data_dir = '/data2/Ridgecrest'
out_root = '/data4/bigdata/zhouyj/Example_templates'
temp_pha = 'input/example_pad.temp'

# cut template data
shutil.copyfile('config_example.py', os.path.join(mess_dir, 'config.py'))
os.system("python {}/cut_template_sac.py \
    --data_dir={} --temp_pha={} --out_root={}"\
    .format(mess_dir, data_dir, temp_pha, out_root))

