<template>
    <form id="movieForm" @submit.prevent="saveMovie">
        <fieldset class="form-group">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input id="title" type="text" name="title" class="form-control" />
            </div>
            <div class="form-group mb-3">
                <label for="description" class="form-label">Description</label>
                <input id="description" type="text" name="description" class="form-control" />
            </div>
            <div class="form-group mb-3">
                <input id="poster" type="file" name="poster" class="form-control" accept="image/jpeg, image/jpg, image/png" />
            </div>
        </fieldset>
        <div class = "form-group">
            <button type="submit" class ="btn btn-primary">Submit</button>
        </div>
    </form>
</template>

<script setup>
    import { ref, onMounted } from "vue";
    let csrf_token = ref("");

    onMounted(() => {
        getCsrfToken();
    });

    function saveMovie() {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
            });

}

    function getCsrfToken() {
    fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
}
</script>