import sys
from mindspore.train._utils import read_proto

model = read_proto(sys.argv[1])

json_file = "mindir.json" if len(sys.argv) <= 2 else sys.argv[2]

sourceFile = open(json_file, 'w')

print(model, file=sourceFile)

print(f"converted MINDIR model {sys.argv[1]} to {json_file}.")

sourceFile.close()