import tarfile


with tarfile.open("test.tar.gz", "w:gz") as tr:
    tr.add('subdir')


with tarfile.open("test.tar.gz", 'r:gz') as tr:
    
    import os
    
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tr, path="test_tar")
    with tr.extractfile('subdir/sub_txt.txt') as f:
        print(f.read())
