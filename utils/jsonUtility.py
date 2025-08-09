import json
import os



class JsonUtility:
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    save_directory = os.path.join(parent_dir, "Data")
    save_file = "tasks.json"
    complete_save_file_path = os.path.join(save_directory, save_file)


    def __init__(self):
        """Initializes the JsonUtility class."""
        specified_save_directory = JsonUtility.get_save_directory()

        

    @staticmethod
    def load_json(file_path):
        """Load JSON data from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_json(data, file_path):
        """Save JSON data to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)






    @staticmethod
    def get_save_directory(i=0):
        """Get the directory where JSON files are saved."""

        #stop condition if reccursivity goes too deep
        if i > 2:
            print("Error: Could not find a valid save directory after 3 attempts.")
            return None

        # get the config file path
        config_path = os.path.join(JsonUtility.parent_dir, "config.json")
        print("========> " + config_path)

        # default values for if there is an issue with default config file
        save_directory = "test"
        save_file = JsonUtility.save_file
        complete_save_file_path = JsonUtility.complete_save_file_path

        # Resilience about config file + default values settings for config file (is this considered a fixture?)
        with open(config_path, 'r', encoding='utf-8') as file:
            cfg_content = file.read()
            print("CFG : " + cfg_content + " " + str(len(cfg_content)))
            if len(cfg_content) == 0:
                print(f"Config file is empty: {config_path}")
            else:
                with open(config_path, 'r', encoding='utf-8') as file:
                    Config_json = json.load(file)
                save_directory = Config_json.get("saveTo")
                save_file = Config_json.get("save_name")
                complete_save_file_path = os.path.join(save_directory, save_file)

        # If the save directory is not set or is invalid, use default values
        if save_directory in ["", None, "test"]:
            # Use default values if config is missing or invalid
            save_directory = os.path.join(JsonUtility.parent_dir, "Data")
            save_file = "tasks.json"
            complete_save_file_path = os.path.join(save_directory, save_file)
            if not os.path.exists(save_directory):
                print(f"Creating save directory: {save_directory}")
                os.makedirs(save_directory)
            JsonUtility.set_save_directory(save_directory, save_file, complete_save_file_path)
            with open(complete_save_file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4, ensure_ascii=False)
            #if there was an issue, reccursively retry with all config set by default
            return JsonUtility.get_save_directory(i+1)
        else:
            # If the save directory is valid, set the class variables and return complete save path
            JsonUtility.save_directory = save_directory
            JsonUtility.save_file = save_file
            JsonUtility.complete_save_file_path = complete_save_file_path
            print(f"Save set to: {JsonUtility.complete_save_file_path}")
            return complete_save_file_path
    


    @staticmethod
    def set_save_directory(dir, name, complete):
        """Set the directory where JSON files are saved."""
        config = {
            "saveTo": dir,
            "save_name": name,
            "complete_path": complete
        }
        config_path = os.path.join(JsonUtility.parent_dir, "config.json")
        with open(config_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4, ensure_ascii=False)

