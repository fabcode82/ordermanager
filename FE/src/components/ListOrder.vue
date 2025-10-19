
<template>

        <!-- ORDERS LIST -->
        <div class="card">
            <h2 class="filter-title">Elenco Ordini (<span id="orderCount">{{orders.length}}</span> Trovati)</h2>



            <div id="ordersTableContainer" class="table-container ">
                <table class="orders-table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome Ordine</th>
                            <th>Descrizione</th>
                            <th>Data (yyyy-mm-dd)</th>
                             <th>nr prods</th>
                             <th></th>
                        </tr>
                    </thead>
                    <tbody id="ordersTableBody">

                        <SingleOrder v-for="order in orders" :key="order.id" :order="order" />                 
                    </tbody>
                </table>
            </div>
        </div>
</template>

<script>
import SingleOrder from "@/components/SingleOrder.vue";
export default {
  name: "ListOrder",
  components: {
        SingleOrder,
    },
  props: {
    orders: {
      type: Array,
      required: true,
    },
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

        /* TABELLA ORDINI */
        .table-container {
            overflow-x: auto;
        }
        .orders-table {
            min-width: 100%;
            border-collapse: collapse;
            border-spacing: 0;
            border-top: 1px solid #e5e7eb; /* divide-y gray-200 */
        }
        .orders-table thead th {
            padding: 0.75rem 1.5rem; /* px-6 py-3 */
            background-color: #f9fafb; /* bg-gray-50 */
            text-align: left;
            font-size: 0.75rem; /* xs */
            font-weight: 500;
            color: #6b7280; /* gray-500 */
            text-transform: uppercase;
            letter-spacing: 0.05em; /* tracking-wider */
        }
        .orders-table tbody {
            background-color: white;
        }
        .orders-table tbody tr {
            border-bottom: 1px solid #e5e7eb;
        }
        .orders-table tbody tr:hover {
            background-color: #f9fafb; /* hover:bg-gray-50 */
            transition: background-color 0.1s;
        }
        .orders-table td {
            padding: 1rem 1.5rem; /* px-6 py-4 */
            font-size: 0.875rem; /* sm */
            color: #1f2937; /* gray-900 */
        }
        .orders-table td:nth-child(1) { /* Nome Ordine */
            font-weight: 500;
            white-space: nowrap;
        }
        .orders-table td:nth-child(2) { /* Descrizione */
            color: #6b7280; /* gray-500 */
            /* Permette alla descrizione di andare a capo */
            white-space: normal; 
        }
        .orders-table td:nth-child(3) { /* Data */
            color: #6b7280;
            white-space: nowrap;
        }
</style>
