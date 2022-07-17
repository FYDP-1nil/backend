gen: 
	python3 -m grpc_tools.protoc -I ../proto/ --python_out=. --grpc_python_out=. ../proto/stats.proto;

run: 
	python3 service.py 