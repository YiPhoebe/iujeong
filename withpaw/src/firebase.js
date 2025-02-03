// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCkE13a9gZAmItWlQuofaGaDVYPRHdbx_A",
  authDomain: "withpaw-4d0fa.firebaseapp.com",
  projectId: "withpaw-4d0fa",
  storageBucket: "withpaw-4d0fa.firebasestorage.app",
  messagingSenderId: "295723869922",
  appId: "1:295723869922:web:aabd391939bffc09a8e0bb",
  measurementId: "G-4G42RXB0S6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);