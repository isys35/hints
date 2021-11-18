Код, чтобы сгенерировать код Python из `protobufs`:

```shell
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
```
<ul>
    <li> <b><i>python -m grpc_tools.protoc</i></b> запускает компилятор, который генерирует код Python из кода Protobuf </li>
    <li> <b><i>-I ../protobufs</i></b> сообщает компилятору, где найти файлы, которые импортирует код Protobuf. </li>
    <li> <b><i>--python_out =. --grpc_python_out =.</i></b>  сообщает компилятору, куда выводить файлы Python </li>
    <li> <b><i>../protobufs/recommendations.proto</i></b>  это путь к файлу protobuf, который будет использоваться для генерации кода Python. </li>
</ul>