from pydantic import BaseModel


class ReceiptItem(BaseModel):
    item_name: str | None
    quantity: int | None
    unit_price: int | None
    type: int | None


class Store(BaseModel):
    name: str | None
    address: str | None
    telephone: str | None


class ReceiptData(BaseModel):
    store: Store | None
    datetime: str | None
    items: list[ReceiptItem] | None
    tax: int | None
    tax_included_price: int | None


class AnalyzeResult(BaseModel):
    ocr: str
    result: ReceiptData
