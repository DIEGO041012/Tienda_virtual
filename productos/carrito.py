class Carrito:
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto, cantidad=1):
        id = str(producto.id)
        if id not in self.carrito:
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": cantidad,
                "imagen": producto.imagen.url if producto.imagen else ''
            }
        else:
            self.carrito[id]["cantidad"] += cantidad
        self.guardar()

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def obtener_total(self):
        total = 0
        for item in self.carrito.values():
            total += float(item["precio"]) * item["cantidad"]
        return total

    def contar_items(self):
        return sum(item["cantidad"] for item in self.carrito.values())
