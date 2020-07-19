<template>
    <div>
        <div>
            <img :src="captured" width="100%" height="500px" style="object-fit: contain"/>
        </div>
        <div>
            <input type="file" accept="image/*" @change="onFileChange"/>
            <button @click="onSubmit">SUBMIT</button>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                captured: "",
                capturedFile: null,
            }
        },
        methods: {
            onFileChange(e) {
                const file = e.target.files[0];
                this.capturedFile = file;
                const reader = new FileReader();
                const self = this;
                reader.onloadend = function () {
                    self.captured = this.result;
                }
                reader.readAsDataURL(file);
            },
            onSubmit() {
                const fd = new FormData();
                fd.append('file', this.capturedFile);
                axios.post('http://localhost:8081/poster/upload', fd).then((result) => {
                    console.log(result);
                })
            }
        }
    }
</script>