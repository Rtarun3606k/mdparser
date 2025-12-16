# Fenced Div Test Suite

---

## 1. Basic fenced div

::: hero
This is a basic hero section.
:::

---

## 2. Fenced div with Tailwind classes

::: hero bg-blue-500 text-white p-6 rounded
This hero has Tailwind classes.
:::

---

## 3. Fenced div with heading and paragraph

::: section bg-gray-100 p-4

# Welcome

This section contains a heading and paragraph.
:::

---

## 4. Fenced div with inline markdown

::: card border p-4
This has **bold**, _italic_, and `inline code`.
:::

---

## 5. Fenced div with list

::: list-box bg-white p-4

- Item one
- Item two
- Item three
  :::

---

## 6. Fenced div with ordered list

::: steps bg-gray-50 p-4

1. Step one
2. Step two
3. Step three
   :::

---

## 7. Nested fenced divs (IMPORTANT)

::: outer bg-gray-200 p-6
Outer content starts.

::: inner bg-white p-4
Inner content inside nested div.
:::

Outer content ends.
:::

---

## 8. Fenced div with code block

::: code-wrapper bg-black p-4

```python
def hello():
    print("hello world")
```
