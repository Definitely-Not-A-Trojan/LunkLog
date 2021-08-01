# Database
## MongoDB https://www.mongodb.com/

### Databases
Two main databases, one for release and one for development.
  - LunkLog_Develop
  - LunkLog_Release

### Collections (Tables)
  - **users**
    - User login and basic communication info.
      - (objectId) user_id
      - (string) username
      - (int32) age
      - (int32) height
      - (string) email_address
      - (string) phone_number
      - (date) date_joined

  - **users.options**
    - Users options
      - (bool) profile_public
      - (bool) 2fa_enabled
      - (string enum) units
      - (bool) email_updates_enabled

  - **users.friends**
    - Stores users friends list, privacy, and associations with friends.
      - (objectId) user_id
      - (object array) friends
      - (object array) blocked_users

  - **users.groups**
    - Stores users groups, privacy, and association with the group. 
      - (objectId) group_id
      - (object array) users
      - (objectId array) blocked_users
      - (enum) privacy

  - **users.goals**
    - Stores user defined goals.
      - (objectId) user_id
      - (object array) goals

  - **users.achievements**
    - Stores user achieved achievements.
      - (objectId) user_id
      - (object array) achievements

  - **groups**
    - Stores all user groups
      - (objectId) group_id
      - (string) group_name
      - (string) group_description
      - (string) group_motto
      - (int32) user_count

  - **achievements**
    - Stores all possible achievements.
      - (string) name
      - (string) description

  - **measurements**
    - Weight, body fat percentage, height, body part circumference measurements.
      - (objectId) user_id
      - (string) name
      - (double) measurement
      - (string enum) units
      - (bool) manual_entry


  - **sets**
    - Logging for exercise execution.
      - (objectId) user_id
      - (int32) rep
      - (double) weight
      - (double) time
      - (bool) personal_record
      - (string) comment
      - (date) date


  - **exercises**
    - Exercise information, targeted muscle groups.
      - (string) name
      - (string enum) primary_target
      - (string array) muscle_groups
      - (string array) equipment_required
      - (objectId) created_by
