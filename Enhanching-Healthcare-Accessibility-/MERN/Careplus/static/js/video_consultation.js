// video_consultation.js

const localVideo = document.getElementById('localVideo');
const remoteVideo = document.getElementById('remoteVideo');
const startButton = document.getElementById('startButton');
const hangupButton = document.getElementById('hangupButton');
const signalingUrl = '/Careplus/views/';

let localStream;
let peerConnection;
let offerSent = false;

const configuration = { iceServers: [{ urls: 'stun:stun.l.google.com:19302' }] };

async function getLocalStream() {
  try {
    localStream = await navigator.mediaDevices.getUserMedia({ audio: true, video: true });
    localVideo.srcObject = localStream;
  } catch (error) {
    console.error('Error getting user media:', error);
  }
}

getLocalStream();

startButton.addEventListener('click', () => {
  startButton.disabled = true;
  hangupButton.disabled = false;

  peerConnection = new RTCPeerConnection(configuration);

  localStream.getTracks().forEach((track) => {
    peerConnection.addTrack(track, localStream);
  });

  peerConnection.ontrack = (event) => {
    remoteVideo.srcObject = event.streams[0];
  };

  peerConnection.onicecandidate = (event) => {
    if (event.candidate) {
      const candidate = {
        type: 'candidate',
        candidate: event.candidate
      };
      sendSignal(candidate);
    }
  };

  if (!offerSent) {
    sendOffer();
    offerSent = true;
  }
});

hangupButton.addEventListener('click', () => {
  peerConnection.close();
  startButton.disabled = false;
  hangupButton.disabled = true;
});

function sendOffer() {
  peerConnection.createOffer().then((offer) => {
    return peerConnection.setLocalDescription(offer);
  }).then(() => {
    const offerData = {
      type: 'offer',
      sdp: peerConnection.localDescription.sdp
    };
    sendSignal(offerData);
  });
}

function sendSignal(data) {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', signalingUrl, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = () => {
    if (xhr.status === 200) {
      console.log('Signal sent successfully');
    }
  };
  xhr.send(JSON.stringify(data));
}
// video_consultation.js

document.querySelector('form').addEventListener('submit', function(event) {
  event.preventDefault();
  const roomID = document.getElementById('room_id').value;
  window.location.href = `/video_call/${roomID}/`;  // Redirect to video call page with room ID
});
