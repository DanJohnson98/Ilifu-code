import pickle

def save_run_info(obj):
    try:
        with open("run_parameters", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

obj = {"num_per_run": 5,
       "n_burn": 100,
       "n_run": 100,
       "threadCount": 8
       }

save_run_info(obj)
