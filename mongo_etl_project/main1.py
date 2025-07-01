from extract.loader1 import insert_projects_from_file
from extract.mongo_connector1 import fetch_projects_from_mongo
from transform.profile_mapper import map_customer_profiles
from load.writer1 import save_profiles_to_csv
from load.sql_loader import load_to_mysql, load_to_sqlserver

def main():
    insert_projects_from_file()
    projects = fetch_projects_from_mongo()
    print(f"🔍 Retrieved {len(projects)} project(s) from MongoDB.")

    profiles = map_customer_profiles(projects)
    save_profiles_to_csv(profiles)

    load_to_mysql(projects)
    load_to_sqlserver(projects)

    print("🎉 All tasks complete.")

if __name__ == "__main__":
    main()
