# Bi-LSTM-CRF-CWS
Bi-LSTM+CRF for Chinese word segmentation


## Usage
Have tensorflow 1.2 installed.
### Command Step by Step
* Preprocessing <br>
    
    *python preprocess.py --rootDir \<ROOTDIR> --corpusAll Corpora/all.txt --resultFile pre_chars_for_w2v.txt*
    
    *python getpinyin.py*
    
    *python getwubi.py*
    
    ROOTDIR is the absolute path of your corpus. Run *python preprocess.py -h* to see more details.
    
* Word2vec Training <br>
    
    *./third_party/word2vec -train pre_chars_for_w2v.txt -save-vocab pre_vocab.txt -min-count 3*
    
    *./third_party/word2vec -train pre_pinyin_for_w2v.txt -save-vocab pre_vocab_pinyin.txt -min-count 3*
    
    *./third_party/word2vec -train pre_wubi_for_w2v.txt -save-vocab pre_vocab_wubi.txt -min-count 3*
    
    
    *python SentHandler/replace_unk.py pre_vocab.txt pre_chars_for_w2v.txt chars_for_w2v.txt*
    
    *python SentHandler/replace_unk.py pre_vocab_pinyin.txt pre_pinyin_for_w2v.txt pinyin_for_w2v.txt*
    
    *python SentHandler/replace_unk.py pre_vocab_wubi.txt pre_wubi_for_w2v.txt wubi_for_w2v.txt*
    
    
    *./third_party/word2vec -train chars_for_w2v.txt -output char_vec.txt \\<br>
    -size 100 -sample 1e-4 -negative 0 -hs 1 -binary 0 -iter 5*
    
    *./third_party/word2vec -train pinyin_for_w2v.txt -output pinyin_vec.txt \\<br>
    -size 100 -sample 1e-4 -negative 0 -hs 1 -binary 0 -iter 5*
    
    *./third_party/word2vec -train wubi_for_w2v.txt -output wubi_vec.txt \\<br>
    -size 100 -sample 1e-4 -negative 0 -hs 1 -binary 0 -iter 5*
    
    First off, the file **word2vec.c** in third_party directory should be compiled (see third_party/compile_w2v.sh). Then word2vec counts the characters which have a frequency more than 3 and saves them into file **pre_vocab.txt**. After replacing with **"UNK"** the words that are not in pre_vocab.txt, finally, word2vec training begins.
    
* Generate Training Files <br>
    
    *python pre_train.py --corpusAll Corpora/pku/train-all.txt --vecpath char_vec.txt \\<br>
    --train_file Corpora/pku/train.txt --test_file Corpora/pku/test.txt*
    
    Run *python pre_train.py -h* to see more details.
    
* Training <br>
    
    *python ./CWSTrain/lstm_crf_train.py --train_data_path Corpora/pku/train.txt \\<br>
    --test_data_path Corpora/pku/test.txt --word2vec_path char_vec.txt*
    
    Arguments of *lstm_cnn_train.py* are set by **tf.app.flags**. See the file for more args' configurations.
