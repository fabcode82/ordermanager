
<template>
    <tr>
        <td>{{order.id}}</td>
        <td>{{order.name}}</td>
        <td>{{order.description}}</td>
        <td>{{order.date}}</td>
        <td>{{order.items.length}}</td>
        <router-link :to="'/order/' + order.id">

        <td>Detail</td>
        </router-link>
    </tr>
</template>

<script>


export default {
  name: "SingleOrder",
  props: {
    order: {
      type: Object,
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
