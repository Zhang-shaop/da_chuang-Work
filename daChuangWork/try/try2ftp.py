import pysftp

cnopts=pysftp.CnOpts()

host='10.21.19.232'
port=12344
cinfo={'host':host,'port':port}
with pysftp.Connection(**cinfo,cnopts=cnopts) as sftp:
    file_path='E:/new dachuang/data/1室电压.txt'
    try:
        with sftp.open(file_path,'r') as f:
            print(f.read())
    except Exception as e:
        print('NO found file!')

