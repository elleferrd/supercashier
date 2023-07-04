{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fb066788-6198-4a0f-bb3c-8a5d7f49b69a",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import kasir\n",
    "from kasir import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9b9235a-ed50-417b-bc0f-9e6f1c9fb242",
   "metadata": {},
   "outputs": [],
   "source": [
    "#generate id\n",
    "kasir.Transaksi.generate_id()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3e584af-f8c5-4d14-8b79-fe4f3c42ac2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#add item\n",
    "Transaksi.add_item(\"<id transaksi>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec2d3d0e-bc24-4c32-9c7b-a37c2fc0cb0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#update item \n",
    "Transaksi.update_item_name(\"<item yang ingin diupdate>\", \"<item yang akan diupdate>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6a57123-751a-435a-91b9-3f9d164d0515",
   "metadata": {},
   "outputs": [],
   "source": [
    "#update jumlah item\n",
    "Transaksi.update_item_qty(\"<item yang ingin diupdate>\", <jumlah item>)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b31588c-814b-4db1-be6c-b790e94107ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#update harga item\n",
    "Transaksi.update_item_price(\"<item yang ingin diupdate>\", <harga item>)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ee6c5a4-3710-4bb9-979a-b00bd3f1bee6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#delete item\n",
    "Transaksi.delete_item(\"<item yang ingin diupdate>\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "858377cf-2961-4b20-9db4-f965bbaa9266",
   "metadata": {},
   "outputs": [],
   "source": [
    "#reset transaction\n",
    "Transaksi.reset_transaction()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69b3fca9-7a98-439a-bd74-0b84a7746a0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#check transaction\n",
    "Transaksi.check_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1112567a-c894-49cd-ba78-59c2fb00381c",
   "metadata": {},
   "outputs": [],
   "source": [
    "Transaksi.total_price()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
