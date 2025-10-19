<template>
    <div>

        <!-- <div>Order ID: {{id}}</div> -->
<div id="app" class="app-container">
    
    <div class="max-w-6xl">
        <h1 class="page-title">
            Dettaglio Ordine:  ID: {{order.id}} <span id="orderNameDisplay"></span>
        </h1>
        
        <!-- PULSANTI DI AZIONE -->
        <div class="button-group">
            <a href="/" class="secondary-button">&larr; Torna alla lista ordini</a>
            <button  @click="UpdateOrder" id="toggleEditButton" class="primary-button edit">Modifica Dati</button>
            <button  @click="deleteOrder" id="deleteButton" class="primary-button delete" >Elimina Ordine</button>
        </div>

        <!-- MESSAGGI DI SUCCESSO/ERRORE -->
        <br>
        <div v-if="updated">
            <h4 style="color: #00a135;">(Ordine correttamente aggiornato)</h4>
        </div>
        <div v-if="errorMessage.length" >
            <h4 style="color: #FF0000;">{{errorMessage}}</h4>
        </div>
        <div v-if="loadingOrder">
            <h4>Caricamento ordine in corso...</h4>
        </div>


        <!-- CARD: Dettagli Ordine -->
        <div class="card" style="margin-top: 1.5rem;">
            <h2 class="section-title">Informazioni Ordine</h2>
            
            <form id="orderDetailForm">
                <div class="detail-grid">
                    <!-- Nome Ordine -->
                    <div>
                        <strong for="inputName">Nome Ordine</strong>
                    <input v-model="order.name" type="text" id="inputName" class="form-input"  required>
                    </div>

                    <!-- Data dell'Ordine -->
                    <div>
                        <strong for="inputDate">Data dell'Ordine</strong>
                        <input v-model="order.date" type="date" id="inputDate" class="form-input"  required>
                    </div>
                    
                    <!-- Descrizione  -->
                    <div style="grid-column: 1 / -1;">
                        <strong for="inputDescription">Descrizione</strong>
                        <textarea v-model="order.description"  id="inputDescription" class="form-textarea"  required></textarea>
                    </div>


                </div>
            </form>
        </div>

        <!-- Prodotti Legati all'ordine -->
        <div class="card">
            <h2 class="section-title">Articoli</h2>
            
            <div class="table-container">
                <table class="orders-table">
                    <thead>
                        <tr>
                            <th>Prodotto</th>
                            <th >Prezzo Unitario (€)</th>
                            <th >Quantità</th>
                            <th>Elimina</th>
                        </tr>
                    </thead>
                    <tbody id="itemsTableBody">
                        <tr v-for="(item, index) in order.items" :key="index">
                            
                            <td>{{item.product_name}}</td>
                            <td >{{item.product_price}}</td>
                            <td >
                                <input v-model="item.quantity" type="number" id="inputName" class="form-input"  required>
                                <!-- {{item.quantity}} -->
                            </td>
                            <td> 
                                <button @click="deleteItem(item.product_id)" id="ProductdeleteButton" class="primary-button delete" >Elimina</button>
                            </td>
                        </tr>
                    </tbody>

                </table>
            </div>
        </div>
    </div>
</div>



    </div>
</template>





<script >

import { axios } from "@/common/api.service.js";
import {API_URL} from "@/common/endpoints.js";

export default {
  name: "OrderEditView",
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      order: {},
      params: {},
      updatedOrder: {},
      errorMessage: "",
      updated: false,
      loadingOrder: false,
    };
  },
  methods: {

    deleteItem(id){
        console.log("Deleting item...");
        console.log(id);
        this.order.items = this.order.items.filter(item => item.product_id !== id);
        console.log(this.order.items);
    },

    async getOrder() {

      this.loadingOrder = true;
      try {

        const response = await axios.get(API_URL + "orders/" + this.id,  );
        console.log(response.data);
        this.order = response.data
        this.loadingOrder = false;

      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },

    async deleteOrder() {
      try {
        await await axios.delete(API_URL + "orders/" + this.id + "/");
        this.$router.push({
          name: "home",
        });
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
        this.errorMessage = "ERROR: " + error.response.statusText;
        console.log(error.response);

      }
    },
    async UpdateOrder() {
      console.log("Updating order...");
      this.loadingOrder = true;
      this.updated = false;
      this.errorMessage = "";

      let updated_items = []
      updated_items = this.order.items.map(item => {
        return {
          product: item.product_id,
          quantity: item.quantity
        };
      });
      this.updated_order =  {
        name: this.order.name,
        description:  this.order.description,
        date: this.order.date,
        items_in: updated_items
        }
      console.log("UPDATED ORDER:");
      console.log(this.updated_order);
      try {


        let response = await axios.patch(API_URL + "orders/" + this.id + "/",  this.updated_order );
        this.loadingOrder = false;

        console.log("Order updated successfully.");
        console.log(response.data);
        this.updated = true;
        this.errorMessage = "";
        // this.$router.go(0);
      } catch (error) {
        this.errorMessage = "ERROR: " + error.response.statusText;
        console.log(error.response);

        alert(error.response.statusText);

      }
    },
  },
  created() {
    document.title = "Orders - ILIAD";
    this.getOrder();
  },
};
</script>




<style scoped>


        :root {
            font-family: Arial, sans-serif;
        }
        body {
            margin: 0;
            background-color: #f7f7f7; 
        }
        .app-container {
            min-height: 100vh;
            padding: 1rem; 
        }
        .max-w-6xl {
            max-width: 1024px; 
            margin-left: auto;
            margin-right: auto;
        }

        /* Intestazione */
        .page-title {
            font-size: 2.25rem; 
            font-weight: 800; 
            color: #1f2937; 
            margin-bottom: 1.5rem; 
            padding-bottom: 0.5rem; 
            border-bottom: 1px solid #e5e7eb; 
        }

        /* CARD Generale */
        .card {
            background-color: white;
            padding: 1.25rem; 
            border-radius: 0.75rem; 
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); 
            margin-bottom: 2rem; 
        }
        
        /* Titoli Interni */
        .section-title {
            font-size: 1.25rem; 
            font-weight: 600; 
            color: #4b5563; 
            margin-bottom: 1rem; 
        }

        /* Dettagli (Layout a griglia per le info) */
        .detail-grid {
            display: grid;
            grid-template-columns: repeat(1, minmax(0, 1fr));
            gap: 1.5rem; /* gap-6 */
            margin-bottom: 1.5rem;
        }
        @media (min-width: 640px) { /* sm breakpoint */
            .detail-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }
        }

        .detail-item strong {
            display: block;
            font-size: 0.875rem; /* sm */
            font-weight: 500;
            color: #4b5563; /* gray-700 */
            margin-bottom: 0.25rem;
        }
        .detail-item span {
            display: block;
            font-size: 1rem; 
            color: #1f2937; /* gray-900 */
        }
        
        /* INPUT & TEXTAREA */
        .form-input, .form-textarea {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #d1d5db; /* border-gray-300 */
            border-radius: 0.5rem;
            transition: all 0.2s;
            background-color: #f9fafb; /* gray-50 - per distinguerli quando disabilitati */
            color: #1f2937;
        }
        .form-input:focus, .form-textarea:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.5);
            border-color: #3b82f6;
            background-color: white; /* Bianco quando attivo */
        }
        .form-textarea {
            min-height: 80px;
            resize: vertical;
        }
        .form-input:disabled, .form-textarea:disabled {
            border-color: transparent; /* Nasconde il bordo se disabilitato */
            cursor: default;
        }


        /* Pulsanti Azione */
        .button-group {
            display: flex;
            gap: 1rem; /* Spazio tra i pulsanti */
            margin-top: 1rem;
            flex-wrap: wrap;
        }
        
        /* Bottone Torna Indietro e Modifica/Salva (Secondario/Primario) */
        .secondary-button, .primary-button {
            display: inline-block;
            padding: 0.5rem 1rem; 
            font-weight: 500; 
            border-radius: 0.5rem; 
            transition: background-color 0.15s ease-in-out, opacity 0.3s;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
            border: 1px solid transparent;
        }
        
        .secondary-button {
            background-color: #f3f4f6; /* gray-100 */
            color: #4b5563; /* gray-700 */
            border-color: #d1d5db;
        }
        .secondary-button:hover {
            background-color: #e5e7eb; /* gray-200 */
        }
        
        .primary-button.edit {
            background-color: #2563eb; /* blue-600 */
            color: white;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); 
        }
        .primary-button.edit:hover:not(:disabled) {
            background-color: #1d4ed8; /* blue-700 */
        }
        .primary-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }


        .primary-button.delete {
            background-color: #ef4444; /* red-500 */
            color: white;
        }
        .primary-button.delete:hover:not(:disabled) {
            background-color: #dc2626; /* red-600 */
        }
        
        /* TABELLA ARTICOLI */
        .table-container {
            overflow-x: auto;
            margin-top: 1rem;
        }
        .orders-table { 
            min-width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            border-top: 1px solid #e5e7eb; 
        }
        .orders-table thead th {
            padding: 0.75rem 1.5rem; 
            background-color: #f9fafb; 
            text-align: left;
            font-size: 0.75rem; 
            font-weight: 500;
            color: #6b7280; 
            text-transform: uppercase;
            letter-spacing: 0.05em; 
        }
        .orders-table tbody {
            background-color: white;
        }
        .orders-table tbody tr {
            border-bottom: 1px solid #e5e7eb;
        }
        .orders-table tbody tr:hover {
            background-color: #f9fafb; 
            transition: background-color 0.1s;
        }
        .orders-table td {
            padding: 1rem 1.5rem; 
            font-size: 0.875rem; 
            color: #1f2937; 
        }
        .orders-table td.total-cell {
            font-weight: 700;
            background-color: #f3f4f6;
        }
        .text-right {
            text-align: right;
        }
        .text-center {
            text-align: center;
        }


</style>