from datasets import load_dataset, DatasetDict
dataset_name = "imagenet-1k" # maybe find smaller one?

# download to memory
train_dataset = load_dataset(dataset_name)
train_dataset.save_to_disk('imagenet')