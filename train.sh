python download_images.py && python convert_images.py
cd stylegan2-ada-pytorch/
python dataset_tool.py --source=../uniform_images --dest=../training_data.zip
python train.py --outdir=../training-runs --gpus=1 --data=../training_data.zip --resume=ffhq256 --snap=1 --metrics=none --gamma=0.1
