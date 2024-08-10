---

description: Interações com a tag `input` com o atributo `type="radio"`.

---

Interações com `input` com o atributo `type="radio"`.

## Lendo o elemento

### Obtendo a classe correta do elemento para o xpath

```python linenums="1"
my_radio = web.radio_input('//*[id="myRadioInput"]')
type(my_radio)
```

```python title="Saída"
fastrpa.core.elements.RadioInputElement
```

### Tentando obter um `RadioInputElement`

```python linenums="1"
my_radio = web.file_input('//*[id="myRadioInput"]')
type(my_radio)
```

```python title="Saída"
fastrpa.core.elements.RadioInputElement
```

## Referência

### Obter todas as opções de rádio

Dado um elemento de rádio, você pode consultar outras opções com o mesmo atributo `@name`. Este método retornará um dicionário com os valores dos rádios e seu respectivo texto de rótulo associado.

```python linenums="1"
my_radio.options
```

```python title="Saída"
{'option1': 'Default radio',
 'option2': 'Second default radio'}
```

### Obter todos os valores das opções de rádio

```python linenums="1"
my_radio.options_values
```

```python title="Saída"
['option1', 'option2']
```

### Obter todos os rótulos das opções de rádio

Este método retornará todos os textos dos rótulos que apontam para elementos de rádio com o mesmo `@name` do elemento de rádio original.

```python linenums="1"
my_radio.options_labels
```

```python title="Saída"
['Default radio', 'Second default radio']
```

### Selecionar uma opção de rádio pelo rótulo

Seguindo a mesma regra, você pode selecionar outro rádio no formulário com o mesmo `@name` do elemento de rádio original.

```python linenums="1"
my_radio.select('Second default radio')
```

### Selecionar uma opção de rádio pelo valor

```python linenums="1"
my_radio.select(value='option1')
```

### Apenas ativar o elemento de rádio original

```python linenums="1"
my_radio.click()
```

### Verificar se os rádios possuem alguma opção

Para verificar por rótulo e valor.

```python linenums="1"
'Other option' in my_radio
```

```python title="Saída"
False
```

### Verificar se os rádios possuem algum rótulo de opção

```python linenums="1"
my_radio.has_option('Other option')
```

```python title="Saída"
False
```

### Verificar se os rádios possuem algum valor de opção

```python linenums="1"
my_radio.has_option(value='3')
```

```python title="Saída"
False
```

### Imprimir as opções do rádio

!!! warning "Extra necessário!"
    Para usar este método, você precisa instalar os extras **debug**, como [mostrado aqui](../index.md#installation), com o comando `pip install "fastrpa[debug]"`.

```python linenums="1"
my_radio.print()
```

```python title="Saída"
[@id="myRadioInput"]
├── [1] Option 1
├── [2] Option 2
├── [3] Option 3
└── [4] Option 4
```
