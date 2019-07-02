# Sentiment_Classifier
**This Project support sentiment classification for binary as well as multi class classification**

The project has the following structure:

    Sentiment_Classifier                                  
                        |---
                            sentiment_analysis            
                                |----
                                    |---data
                                    |---preprocessor
                                    |---feature_extracction
                                    |---model
                                    |---saved_instance
                                    |---notebook
                                    |---config.py
                                    |---__main__.py
                                    
                        |---app.py
                        |---requirement.txt
                        |---README.md
                            
                            
       
 data : consist of datafile and dataloader module. 
 
       - the datafile consist of the dataset .
 preprocessor : module for text pre-processing .
 
 feature_extraction : module for extracting feature from the processed data.
 
 model : module responsible for training model on the extracted feature.
  
 saved_instance : stores the trained model and feature vectorizer on the disk .
 
 notebook : For detailed understanding of techniques use in training model check this one out.
 
`config.py` :  This config file is needed to be initialize before running `__main__.py` .

`__main__.py` : This file is needed to be run to train the model .

`app.py` : Will open an endpoint for  client .



