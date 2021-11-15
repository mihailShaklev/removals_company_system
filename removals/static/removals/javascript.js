function delete_job(jobId) {

   if(confirm("Are you sure you want to delete the job?")) {

       fetch('/delete-job', {
           method:'PUT',
           body:JSON.stringify({
               jobId: jobId
           })
       });

      document.querySelector(`#row${jobId}`).style.display = 'none';
      alert("Entry was deleted!");

   }
}


function show_edit_profile() {

   document.querySelector("#edit_profile").style.display = 'none';
   document.querySelector("#editProfile").style.display = 'block';
}


function cancel_edit_profile() {

   document.querySelector("#pass").value = '';
   document.querySelector("#confirmPass").value = '';
   document.querySelector("#edit_profile").style.display = 'block';
   document.querySelector("#editProfile").style.display = 'none';

   document.querySelector("#checkPass").style.display = 'none';
   document.querySelector("#checkConfPass").style.display = 'none';
   document.querySelector("#emailCheck").style.display = 'none';
   document.querySelector("#passMissMatch").style.display = 'none';
}


function save_profile() {

   let pass1 = document.querySelector("#pass").value;
   let pass2 = document.querySelector("#confirmPass").value;
   let email = document.querySelector("#emailIn").value;

   if (pass1 === "") {

      document.querySelector("#checkPass").style.display = 'block';

   } else if (pass2 === "") {

      document.querySelector("#checkConfPass").style.display = 'block';

   } else if (email === "") {

      document.querySelector("#emailCheck").style.display = 'block';

   } else if (pass1 != pass2) {

      document.querySelector("#passMissMatch").style.display = 'block';

   } else {



      fetch('/update-profile', {
         method:'PUT',
         body:JSON.stringify({
            password:pass1,
            email:email
         })
      });

      document.querySelector("#pass").value = '';
      document.querySelector("#confirmPass").value = '';
      document.querySelector("#edit_profile").style.display = 'block';
      document.querySelector("#editSuccess").style.display = 'block';
      document.querySelector("#checkPass").style.display = 'none';
      document.querySelector("#checkConfPass").style.display = 'none';
      document.querySelector("#emailCheck").style.display = 'none';
      document.querySelector("#passMissMatch").style.display = 'none';
      document.querySelector("#editProfile").style.display = 'none';

   }
}

function send_email() {

   let startDate = document.querySelector("#date1").value;
   let endDate = document.querySelector("#date2").value;
   let mover = "";

   if (document.getElementById("testM")) {

      mover = document.querySelector("#testM").value;
   }

   let user_email = document.querySelector("#user-email").value;

   fetch('/send-mail', {
      method:'POST',
      body:JSON.stringify({
         startDate:startDate,
         endDate:endDate,
         mover:mover,
         userEmail:user_email
      })
   });

   alert("Email was sent!");
}