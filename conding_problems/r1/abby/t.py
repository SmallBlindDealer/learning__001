"""
write a python code to import a pdf document and create vector

indexes based on the given parameters and print those values. ()
Create a function for an api and expose it.

a b c-->

input--> a wer gfgfhg [0, 0 01]
"""



params_file = open("./sample.txt", "r").read()

l = []
for obj in params_file.split("\n"):
    l.extend(obj.split(" "))

l = list(set(l)).sort()

vectors_params_idx_data  = {val: idx  for (idx, val) in enumerate(l)}

unique_params_l = len(l)



def return_vector(input_str):
    arr = [0]*unique_params_l

    for obj in input_str(" "):
        if obj in vectors_params_idx_data:
            arr[vectors_params_idx_data[obj]] = 1
    
    return arr




# import flask 


# app = flask()


class APIView:
    ...



class  VectorAPIView(APIView):


    def post(req):
        data = req.data
        input_str = data.get("input_string", None)
        if not input_str:
            return {}, 404
        else:
            return {"data":  return_vector(input_str)}, 200

        ...


app.include("/convert_vector", "POST")
