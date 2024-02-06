# AirBnB Clone - The Console
---
## Project Description
---
- This is a Python project that implements a backend console for an upcoming AirBnB clone. 
- It is a command line interpreter that can create, read, update, and delete instances. 
---
## Table of Contents
---
- [Features](#features)
- [Commands](#commands)
- [Available Models](#available-models)
- [Usage](#usage)
  - [Interactive Mode](#interactive-mode)
  - [Non-Interactive Mode](#non-interactive-mode)
  - [Examples](#examples)
- [Testing](#testing)
- [Authors](#authors)
---
<a id="features"></a>
## Features
---
- Can create new instances of classes
- Display instances
- Delete instances
- List instances of a specified class
- Update instances with new attributes
- Stores instances in a JSON file
- Supports serialization and deserialization
---
<a id="commands"></a>
## Commands
---
| Command  | Description                                                                                      |
|----------|--------------------------------------------------------------------------------------------------|
| `create` | Creates a new instance of a specified class                                                     |
| `show`   | Displays the string representation of an instance based on class name and ID                     |
| `destroy`| Deletes an instance based on class name and ID                                                   |
| `all`    | Lists string representations of all instances or instances of a specific class                   |
| `update` | Updates an instance by adding or modifying attributes based on class name, ID, attribute name, and new attribute value  |
---
<a id="avaliable-models"></a>
## Available Models
---
| Model       | Default Attributes |
|-------------|--------------------|
| `BaseModel` | `id` `created_at` `updated_at` |
| `Amenity`   | `name` |
| `City`      | `state_id` `name` |
| `Place`     | `city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `price_by_night` `latitude` `longitude` `amenity_ids` |
| `Review`    | `place_id` `user_id` `text` |
| `User`      | `email` `password` `first_name` `last_name` |
---
<a id="usage"></a>
## Usage
---
<a id="interactive-mode"></a>
The console can be started in interactive mode with: \
`$ ./console.py` \
<a id="non-interactive-mode"></a>
You can also pass arguments to the console in non-interactive mode with: \
`$ echo "create User" | ./console.py`
<a id="examples"></a>
### Examples: 
*list all classes in the console*
```
(hbnb)all
[]
```
*create User instance*
```
(hbnb)create User
992f2a78-7f3c-4bba-8446-22ff71931981
```
*display specific User instance with ID*
```
(hbnb)show User 992f2a78-7f3c-4bba-8446-22ff71931981
[User] (992f2a78-7f3c-4bba-8446-22ff71931981) {'id': '992f2a78-7f3c-4bba-8446-22ff71931981', 'created_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609066), 'updated_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609080)}
```
*update User instance attribut 'email' to be 'example@email.com'*
```
(hbnb)update User 992f2a78-7f3c-4bba-8446-22ff71931981 email example@gmail.com
(hbnb)show User 992f2a78-7f3c-4bba-8446-22ff71931981
[User] (992f2a78-7f3c-4bba-8446-22ff71931981) {'id': '992f2a78-7f3c-4bba-8446-22ff71931981', 'created_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609066), 'updated_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609080), 'email': 'example@gmail.com'}
```
*dislay all intances and their respective attribites*
```
(hbnb)all
["[User] (992f2a78-7f3c-4bba-8446-22ff71931981) {'id': '992f2a78-7f3c-4bba-8446-22ff71931981', 'created_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609066), 'updated_at': datetime.datetime(2024, 2, 5, 17, 46, 54, 609080), 'email': 'example@gmail.com'}"]
```
*delete specified User instance with ID*
```
(hbnb)destroy User 992f2a78-7f3c-4bba-8446-22ff71931981
(hbnb)all
[]
```
*quit console*
```
(hbnb)quit

```
---
<a id="testing"></a>
## Testing
---
All tests are in `unittest` format and are inside the /tests directory. 
Run the tests with: \
\
`python3 -m unittest discover tests` 

---
<a id="authors"></a>
## Authors
---
Collin Ballard - https://github.com/Collinb19 \
Evan Markle - https://github.com/EJMarkle

---
