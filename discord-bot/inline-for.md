
# Task 01: List(users) -> List(ids)
```python
## Input
users = [
  {
    'id': 1,
    'name': 'zahra'
  },
  {
    'id': 2,
    'name': 'samin'
  }
]
## Goal
[1, 2]
## Code
[user['id'] for user in users]
```

---

# Task 02: list(users) => dict(name:id)
```python
## Input
users = [
  {
    'id': 1,
    'name': 'zahra'
  },
  {
    'id': 2,
    'name': 'samin'
  }
]
## Goal:
{
  'zahra': 1,
  'samin': 2
}
## Code 01
output = {}
for user in users:
  output[user['name']] = user['id']
## Code 02: Inline for
{user['name']: user['id'] for user in users}
```

---

# Task 03:  dict(user:id) => list(users)
```python
# input(dict)
user_ids = {
  'zahra': 1,
  'samin': 2
}
## output(list)
users = [
  {
    'id': 1,
    'name': 'zahra'
  },
  {
    'id': 2,
    'name': 'samin'
  }
]
## Code

### Step 1

out = []
for user in user_ids.entries():
  out.append(user)
# out => [(zahra,1),(samin,2)]
# name, id = ('zahra', 1)
### Step 2
out = []
# for name, id in user_ids.entries():
for user in user_ids.entries():
  name, id = user
  item = {
    'id': id,
    'name': name
  }
  out.append(item)

# for user in user_ids.entries():
#   name, id = user
#   out.append({
#     'id': id,
#     'name': name
#   })

# for user in user_ids.entries():
#   item = {
#     'id': user[1],
#     'name': user[0]
#   },

## Code 02: Inline for
[{ 'id': user[1],
    'name': user[0]} for user in user_ids.entries()]

[{ 'id': id,
    'name': name} for name, id in user_ids.entries()]
```