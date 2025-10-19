

<template>
  <main>

        <div class="app-container">
            
            <div class="max-w-6xl">
                <h1 class="page-title" style="color: #FF0000;">
                    ILIAD ORDERS MANAGEMENT
                </h1>

                <!-- FILTERS -->
                <div class="card">
                    <h2 class="filter-title">Filtra Risultati</h2>
                    
                    <div class="filter-grid">
                        
                        <!-- Search (Name/Description) -->
                        <div>
                            <label for="searchQuery" class="filter-label">Cerca (Nome/Descrizione)</label>
                            <input 
                                type="text" 
                                id="searchQuery"
                                placeholder="Cerca per nome o descrizione..."
                                class="filter-input"
                                v-model="search"
                                @keyup.enter="getOrders()"
                            >
                        </div>
                        
                        <!-- Date Filter ( -->
                        <div>
                            <label for="dateFilter" class="filter-label">Filtra per Data Esatta</label>
                            <input 
                                type="date" 
                                id="dateFilter"
                                class="filter-input"
                                v-model="date"
                            >
                        </div>

                        <!-- Button (Apply Filters) -->
                        <div class="flex-items-end">
                            <button 
                                id="applyFiltersBtn"
                                class="primary-button"
                                @click="getOrders()"
                                
                            >
                                Applica Filtri
                            </button>
                            <!-- Button (Clean Filters) -->
                            <button 
                                id="cleanFiltersBtn"
                                class="primary-button"
                                @click="cleanFilters()"
                            >
                                Pulisci Filtri
                            </button>
                        </div>
                    </div>
                </div>


                <!-- List of orders -->
                <ListOrder  :orders="orders" />

            </div>
        </div>

  </main>
</template>



<script >

import { axios } from "@/common/api.service.js";
import {API_URL} from "@/common/endpoints.js";
import ListOrder from "@/components/ListOrder.vue";



export default {
  name: "HomeView",
  components: {
    ListOrder,
  },
  data() {
    return {
      orders: [],
      search: "",
      date: "",
      loadingOrders: false,
      params: {}
    };
  },
  methods: {
    async cleanFilters() {
      this.search = "";
      this.date = "";
      this.getOrders();
    },
    async getOrders() {


      this.loadingOrders = true;
      try {
        this.params = {};
        if (this.search) {
          this.params.search = this.search;         
        }
        if (this.date) {
          this.params.date = this.date;         
        }
        const response = await axios.get(API_URL + "orders/",  { params: this.params});
        console.log(response.data);
        this.orders = response.data
        this.loadingOrders = false;

      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    },
  },
  created() {
    document.title = "Orders - ILIAD";
    this.getOrders();
  },
};
</script>


<style scoped>

        /* Base e Reset */
        :root {
            font-family: Arial, sans-serif;
        }
        body {
            margin: 0;
            background-color: #f7f7f7; /* Corrisponde a bg-gray-50 */
        }
        .app-container {
            min-height: 100vh;
            padding: 1rem; /* Corrisponde a p-4 */
        }
        .max-w-6xl {
            max-width: 1024px; /* Corrisponde a max-w-6xl */
            margin-left: auto;
            margin-right: auto;
        }

        /* Intestazione */
        .page-title {
            font-size: 2.25rem; /* 4xl */
            font-weight: 800; /* extabold */
            color: #1f2937; /* gray-900 */
            margin-bottom: 1.5rem; /* mb-6 */
            padding-bottom: 0.5rem; /* pb-2 */
            border-bottom: 1px solid #e5e7eb; /* border-b */
        }

        /* CARD Generale */
        .card {
            background-color: white;
            padding: 1.25rem; /* p-5 */
            border-radius: 0.75rem; /* rounded-xl */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-lg */
            margin-bottom: 2rem; /* mb-8 */
        }
        
        /* FILTRI */
        .filter-title {
            font-size: 1.25rem; /* xl */
            font-weight: 600; /* semibold */
            color: #4b5563; /* gray-700 */
            margin-bottom: 1rem; /* mb-4 */
        }
        .filter-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem; /* gap-4 */
        }
        /* Media query per schermi medi (md:grid-cols-3) */
        @media (min-width: 768px) {
            .filter-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        .filter-label {
            display: block;
            font-size: 0.875rem; /* sm */
            font-weight: 500; /* medium */
            color: #4b5563; /* gray-700 */
            margin-bottom: 0.25rem; /* mb-1 */
        }
        .filter-input {
            width: 100%;
            padding: 0.5rem; /* p-2 */
            border: 1px solid #d1d5db; /* border-gray-300 */
            border-radius: 0.5rem; /* rounded-lg */
            transition: all 0.2s;
        }
        .filter-input:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.5); /* blu */
            border-color: #3b82f6; /* blue-500 */
        }

        .flex-items-end {
            display: flex;
            align-items: flex-end;
        }
        
        /* Bottone Applica */
        .primary-button {
            width: 100%;
            padding: 0.5rem 1rem; /* py-2 px-4 */
            background-color: #2563eb; /* blue-600 */
            color: white;
            font-weight: 500; /* medium */
            border-radius: 0.5rem; /* rounded-lg */
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); /* shadow-md */
            transition: background-color 0.15s ease-in-out;
            border: none;
            cursor: pointer;
        }
        .primary-button:hover:not(:disabled) {
            background-color: #1d4ed8; /* blue-700 */
        }
        .primary-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        /* MESSAGGI DI STATO */
        .status-message {
            text-align: center;
            padding: 2.5rem 0; /* py-10 */
        }
        .status-message.loading {
            color: #2563eb; /* blue-600 */
            font-weight: 500;
        }
        .status-message.empty, .status-message.no-match {
            color: #6b7280; /* gray-500 */
        }
        .hidden {
            display: none !important;
        }
</style>


