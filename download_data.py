from datasets import load_dataset, DatasetDict

# Example: Loading a sample dataset similar to ImageNet (replace with actual dataset as needed)
train_dataset = load_dataset('imagenet-1k', split='train')
# Load 20% of the validation set
val_dataset = load_dataset('imagenet-1k', split='validation')
# Load 20% of the test set
test_dataset = load_dataset('imagenet-1k', split='test')

dataset = DatasetDict({
    'train': train_dataset,
    'validation': val_dataset,
    'test': test_dataset
})

# Save to disk
dataset.save_to_disk('./imagenet_subset')

### Load from disk
### loaded_dataset = DatasetDict.load_from_disk('./imagenet_subset')