| Type                     | Declaration                          | Mixed datatypes | Sliceable / indexable | Duplicate entries | Fixed element order | Hashed | Mutability |
| ------------------------ | ------------------------------------ | --------------- | --------------------- | ----------------- | ------------------- | ------ | ---------- |
| **List**                 | l = [1, "some", 3.45]                | ✅               | ✅                     | ✅                 | ✅                   | ❌      | ✅          |
| **Tuple**                | t = (1, 2)                           | ✅               | ✅                     | ✅                 | ✅                   | ❌      | ❌          |
| **Dictionary keys**      | d = {'some': 11, 'key': "value"}     | ✅               | ❌                     | ❌                 | ❌                   | ✅      | ✅          |
| **Dictionary values**    | d = {1: "some", 2: 22}               | ✅               | ❌                     | ✅                 | by key              | ❌      | ✅          |
| **Set**                  | s = {1, "a"}                         | ✅               | ❌                     | ❌                 | ❌                   | ✅      | ✅          |
| **Frozenset**            | 🤔                                    | 🤔               | 🤔                     | 🤔                 | 🤔                   | 🤔      | 🤔          |
| **String**               | s = "some"                           | ❌               | ✅                     | ✅                 | ✅                   | ❌      | ❌          |
| **Bytearray**            | 🤔                                    | 🤔               | 🤔                     | 🤔                 | 🤔                   | 🤔      | 🤔          |
| **Numpy ndarray**        | n = np.array([[1, 2], [3, 4]])       | ❌               | ✅                     | ✅                 | ✅                   | ❌      | ✅          |
| **Pandas series index**  | s = pd.Series({'a': 11, 9: "value"}) | ❌               | ✅                     | ❌                 | ❌                   | ✅      | ✅          |
| **Pandas series values** | s = pd.Series({'a': 11, 9: "value"}) | ❌               | ✅                     | ✅                 | by index            | ❌      | ✅          |



Todo:
- Modifications (adding, removing, sorting, accessing):