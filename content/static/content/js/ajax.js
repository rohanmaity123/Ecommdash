     
     const imgBox = document.getElementById('image_view')
     const form = document.getElementById('cat_form')

     const name = document.getElementById('nameid')
     const image = document.getElementById('imageid')
     const csrf = document.getElementsByName('csrfmiddlewaretoken')
     console.log(csrf)
     const url = "saveCat/"

     image.addEventListener('change',()=>{
        const img_data = image.files[0]
        const url = URL.createObjectURL(img_data)
        console.log(url)
        imgBox.innerHTML = `<img src="${{url}}" width="100%">`
     })

     form.addEventListener('submit', e =>{
        e.preventDefault()

        const fd = new FormData()
        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('name',name.value)
        fd.append('image',image.files[0])

        $.ajax({
         type:"POST",
         url:url,
         enctype:'multipart/form-data',
         data:fd,
         success:function(responce){
             console.log(responce)
         },
         error: function(error){
            console.log(error)
         },
         cache:false,
         contentType:false,
         processData:false,
     })
     })

     console.log(form)