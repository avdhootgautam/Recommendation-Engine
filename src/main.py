from utils import read_config
from utils import load_dataset
from yaspin import yaspin
def run():
    with yaspin(spinner="dot",text="Loading dataset...",color="cyan") as spinner:
        try:
            config=read_config()
            movie=load_dataset(config['DATASET_PATH']['movie_dataset_path'])
            credit=load_dataset(config['DATASET_PATH']['credit_dataset_path'])
            spinner.ok("✅ ")
            print("LOADING OF DATASET COMPLETED")
        except Exception as e:
            spinner.fail("💥 ")
            print(f"Error loading dataet:: {e}")

if __name__=="__main__":
    run()