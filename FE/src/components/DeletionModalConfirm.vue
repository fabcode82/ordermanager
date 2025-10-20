<template>
        <div v-if="show" class="modal-overlay" @click="cancel">
            <div class="modal-content" @click.stop>
                <div class="modal-header">
                    <h3>Conferma Eliminazione</h3>
                </div>
                <div class="modal-body">
                    <p>Sei sicuro di voler eliminare definitivamente l'ordine ?</p>
                    <p class="warning-text">Questa azione è irreversibile.</p>
                </div>
                <div class="modal-footer">
                    <button class="btn btn-cancel" @click="cancel">
                        Annulla
                    </button>
                    <button class="btn btn-delete" @click="confirmDelete">
                        Elimina
                    </button>
                </div>
            </div>
        </div>
</template>

<script>


export default {
    name: "DeletionModalConfirm",
    emits: ["confirm-delete", "cancel "],
    props: {
    // Controlla se la modale deve essere visibile
    show: {
        type: Boolean,
        required: true
    },

},
    methods: {
        // Emette l'evento per confermare l'eliminazione
        confirmDelete() {
            this.$emit('confirm-delete');
        },
        // Emette l'evento per chiudere/annullare la modale
        cancel() {
            this.$emit('cancel');
        }
    }
}

</script>


<style scoped>

                /* Stili per l'overlay e il centraggio della modale */
                .modal-overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(0, 0, 0, 0.6);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 1000; 
                }
                
                .modal-content {
                    background: #ffffff;
                    border-radius: 8px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                    width: 90%;
                    max-width: 400px;
                    overflow: hidden;
                }
                
                .modal-header {
                    padding: 15px;
                    border-bottom: 1px solid #eee;
                    background-color: #f7f7f7;
                }
                
                .modal-header h3 {
                    margin: 0;
                    color: #333;
                }
                
                .modal-body {
                    padding: 15px;
                }
                
                .modal-body p {
                    margin: 0 0 10px 0;
                    color: #555;
                }

                .warning-text {
                    color: #d9534f;
                    font-weight: bold;
                }
                
                .modal-footer {
                    padding: 15px;
                    border-top: 1px solid #eee;
                    display: flex;
                    justify-content: flex-end;
                    gap: 10px;
                }
                
                .btn {
                    padding: 8px 15px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-weight: 600;
                    transition: background-color 0.2s;
                }
                
                .btn-cancel {
                    background-color: #cccccc;
                    color: #333;
                }
                
                .btn-cancel:hover {
                    background-color: #b3b3b3;
                }
                
                .btn-delete {
                    background-color: #d9534f;
                    color: white;
                }
                
                .btn-delete:hover {
                    background-color: #c9302c;
                }

</style>
