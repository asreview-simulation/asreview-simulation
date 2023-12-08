from asreview.datasets import DatasetManager


def get_dataset_names() -> [str]:
    """
    Returns:

        A list of recognized dataset names.
    """
    dataset_names = list()
    for group in DatasetManager().list():
        for dataset in group["datasets"]:
            dataset_names.append(f"{group['group_id']}:{dataset['dataset_id']}")
    return dataset_names
