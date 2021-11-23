# example and working with big dictionaries
#

ilm_policy = {
    "policy" : {
        "phases" : {
            "hot" : {
                "min_age" : "0ms",
                "actions" : {
                    "rollover" : {
                        "max_size" : "40gb",
                        "max_age" : "3d"
                    }
                }
            },
            "delete" : {
                "min_age" : "30d",
                "actions" : {
                    "delete" : {
                        "delete_searchable_snapshot" : "true"
                    }
                }
            }
        }

    }
}

#print(ilm_policy['policy']['phases']['hot']['actions']['rollover'].keys())

max_size_from_json = ilm_policy['policy']['phases']['hot']['actions']['rollover']['max_size']
max_age_from_json = ilm_policy['policy']['phases']['hot']['actions']['rollover']['max_age']

print(f"Max age is: {max_age_from_json}")
print(f"Max size is: {max_size_from_json}")
