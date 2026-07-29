# Java Access Modifiers

Access Modifiers are keywords in Java that control the **visibility** and **accessibility** of classes, methods, variables, and constructors.

They help implement **Encapsulation** by restricting access to data and methods.

Java provides **four access modifiers**:

- `public`
- `protected`
- `default` (No Modifier)
- `private`

---

# Access Modifier Table

| Access Modifier | Same Class | Same Package | Subclass (Same Package) | Subclass (Different Package) | Different Package (Non-Subclass) |
|-----------------|:----------:|:------------:|:-----------------------:|:----------------------------:|:--------------------------------:|
| **public**      | ✅ | ✅ | ✅ | ✅ | ✅ |
| **protected**   | ✅ | ✅ | ✅ | ✅ | ❌ |
| **default** *(No Modifier)* | ✅ | ✅ | ✅ | ❌ | ❌ |
| **private**     | ✅ | ❌ | ❌ | ❌ | ❌ |

---

# 1. Public

The `public` access modifier provides the **highest level of accessibility**.

A public member can be accessed from:
- The same class
- Any class in the same package
- Any subclass
- Any class in a different package

### Characteristics
- Accessible from anywhere in the project.
- Commonly used for methods that should be available to everyone.
- Can be used with classes, methods, constructors, and variables.

---

# 2. Protected

The `protected` access modifier provides access within the **same package** and to **subclasses outside the package**.

A protected member can be accessed from:
- The same class
- Classes in the same package
- Subclasses in the same package
- Subclasses in different packages

It **cannot** be accessed by a non-subclass class in another package.

### Characteristics
- Supports inheritance.
- Frequently used when subclasses need access to parent class members.
- Cannot be accessed directly from unrelated classes outside the package.

---

# 3. Default (No Modifier)

When no access modifier is specified, Java automatically assigns **default access**, also known as **package-private**.

A default member can be accessed only within the same package.

### Characteristics
- Accessible only inside the package.
- Cannot be accessed from another package.
- Useful when classes within the same package need to share data while hiding it from other packages.

---

# 4. Private

The `private` access modifier provides the **highest level of security**.

A private member can only be accessed within the class in which it is declared.

### Characteristics
- Accessible only inside the same class.
- Not accessible from subclasses.
- Not accessible from other classes, even if they belong to the same package.
- Commonly used to protect sensitive data.

---

# Comparison of Access Modifiers

| Feature | public | protected | default | private |
|---------|:------:|:---------:|:-------:|:-------:|
| Accessible within same class | ✅ | ✅ | ✅ | ✅ |
| Accessible within same package | ✅ | ✅ | ✅ | ❌ |
| Accessible by subclass in same package | ✅ | ✅ | ✅ | ❌ |
| Accessible by subclass in different package | ✅ | ✅ | ❌ | ❌ |
| Accessible by non-subclass in different package | ✅ | ❌ | ❌ | ❌ |

---

# Access Level Order

From **most accessible** to **most restrictive**:

```text
public
   ↓
protected
   ↓
default
   ↓
private
```

---

# Easy Way to Remember

| Modifier | Remember As |
|----------|-------------|
| **public** | Everyone can access it. |
| **protected** | Accessible within the package and by subclasses. |
| **default** | Accessible only within the package. |
| **private** | Accessible only within the same class. |

---

# Why Do We Use Access Modifiers?

- To protect data from unauthorized access.
- To implement Encapsulation.
- To control the visibility of class members.
- To improve security and maintainability.
- To define clear access rules between classes and packages.

---

# Key Points

- Java has **4 access modifiers**.
- `public` is the **least restrictive**.
- `private` is the **most restrictive**.
- `default` is also called **package-private** because access is limited to the same package.
- `protected` is mainly useful when working with **inheritance**.

---

# Summary

| Modifier | Accessibility |
|----------|---------------|
| **public** | Accessible from everywhere. |
| **protected** | Accessible within the package and by subclasses in other packages. |
| **default** | Accessible only within the same package. |
| **private** | Accessible only within the same class. |