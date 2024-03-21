function updateValue(inputId, valueId) {
    var input = document.getElementById(inputId);
    var value = document.getElementById(valueId);
    value.textContent = input.value;
  }

  function selectCell(descritor, valor) {
    // Limpa a seleção anterior na mesma linha
    var rows = document.getElementById('aromasSabores').rows;
    for (var i = 0; i < rows.length; i++) {
      if (rows[i].cells[0].textContent === descritor) {
        for (var j = 1; j < rows[i].cells.length; j++) {
          rows[i].cells[j].classList.remove('selected');
        }
        break;
      }
    }
  
    var cell = document.querySelector(`td[onclick="selectCell('${descritor}', ${valor})"]`);
    if (cell) {
      cell.classList.add('selected');
      document.getElementById(descritor).value = valor;
    }
  }
  
  function iniciarScanner() {
    // Exibe o modal
    document.getElementById('qrCodeModal').style.display = 'block';

    const html5QrCode = new Html5Qrcode("reader");
    const config = { fps: 10, qrbox: { width: 250, height: 250 } };

    // Esta função é chamada quando um QR Code é detectado
    const qrCodeSuccessCallback = (decodedText, decodedResult) => {
      document.getElementById("codigoCafe").value = decodedText;
      html5QrCode.stop().then(() => {
        document.getElementById('qrCodeModal').style.display = 'none';
      }).catch(err => {
        console.error("Falha ao parar o scanner de QR Code", err);
      });
    };

    html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback)
      .catch(err => {
        console.error("Falha ao iniciar o scanner de QR Code", err);
      });
  }

  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("scanBtn").addEventListener("click", iniciarScanner);

    // Fecha o modal quando o usuário clica no (x)
    document.getElementById("closeModal").onclick = function() {
      document.getElementById('qrCodeModal').style.display = "none";
    }
  });