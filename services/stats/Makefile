gen:
	python3 -m grpc_tools.protoc -I ../proto/ --python_out=../gen/ --grpc_python_out=../gen/ ../proto/*.proto;
	sed -i -E 's/^import.*_pb2/from . \0/' ../gen/*.py

gen-mac:
	python3 -m grpc_tools.protoc -I ../proto/ --python_out=../gen --grpc_python_out=../gen ../proto/*.proto;
	gsed -i -E 's/^import.*_pb2/from . \0/' ../gen/*.py

run:
	python3 service.py
