import inkml2ltx as i2l
import os
# test_dir: path to the file of test data to be converted
test_dir = '/YOUR_PATH_without_\'~/\'_/ICFHR_package/CROHME2011_data/CROHME_testGT/CROHME_testGT/'
test_names = [os.path.splitext(name)[0] for name in os.listdir(test_dir)
              if (os.path.isfile(os.path.join(test_dir, name))
                  and os.path.splitext(name)[-1].lower() == '.inkml')]
txt_name = 'batch_output.txt'

for name in test_names:
    i_name = name + '.inkml'
    test_path = os.path.join(test_dir, i_name)
    i2l.inkml2ltx(test_path, txt_name)
