---

descrição: Interações com a tag `input` com atributo [@type="file"].

---

Interações com `input` com atributo `type="file"`.

## Lendo o elemento

### Obtendo a classe de elemento correta para o xpath

```python linenums="1"
my_input = web.element('//*[id="myFileInput"]')
type(my_input)
```

```python title="Saída"
fastrpa.core.elements.FileInputElement
```

### Tentando obter um `FileInputElement`

```python linenums="1"
my_input = web.file_input('//*[id="myFileInput"]')
type(my_input)
```

```python title="Saída"
fastrpa.core.elements.FileInputElement
```

## Referência

### Anexar um arquivo local

```python linenums="1"
my_input.attach_file('/home/user/picture.png')
```

### Anexar um arquivo da web

```python linenums="1"
my_input.attach_file('https://website.com/picture.png')
```
