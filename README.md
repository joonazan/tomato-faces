# Corrupting faces with Stylegan

This repository contains code that downloads images from Google image search and trains Stylegan-ADA with those images. This typically results in faces that have absorbed some features of the training images when trained for 8kimg.

## Running

Run train.sh. You may have to install some python packages to make it work.

## Viewing results

Sample images can be found in training-runs/your-training-run in files named fakesX.png, where X is the number of kimg shown to the network so far. The same folder also contains network snapshots that can be used to explor the whole space.

## Images from image search

By default, the code does not use Google image search. The code exists but you will have to get an API key from Google and create a custom search engine that searches the whole web and has image search enabled.
