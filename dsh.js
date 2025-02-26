document.addEventListener("DOMContentLoaded", function() {
    const content = document.getElementById("content");

    // Handle Navigation Clicks
    document.getElementById("homeTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>Welcome Back to EaglesTX</h2>
            <p>Explore our products and services.</p>
        `;
    });

    document.getElementById("servicesTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>Our Products</h2>
            <ul>
                <li>Routers - $50 <button onclick="processPayment(50)">Buy</button></li>
                <li>Ethernet Cables - $20 <button onclick="processPayment(20)">Buy</button></li>
                <li>Cable Terminators - $10 <button onclick="processPayment(10)">Buy</button></li>
            </ul>
        `;
    });

    document.getElementById("aboutTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>About EaglesTX</h2>
            <p>We provide top-notch internet and networking solutions.</p>
        `;
    });

    document.getElementById("faqsTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>FAQs</h2>
            <p>Find answers to common questions.</p>
        `;
    });

    document.getElementById("adminTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>Admin Login</h2>
            <input type="text" placeholder="Username">
            <input type="password" placeholder="Password">
            <button>Login</button>
        `;
    });

    document.getElementById("userTab").addEventListener("click", () => {
        content.innerHTML = `
            <h2>User Login</h2>
            <input type="text" placeholder="Email">
            <input type="password" placeholder="Password">
            <button>Login</button>
        `;
    });

    document.getElementById("loginBtn").addEventListener("click", () => {
        content.innerHTML = `
            <h2>Login</h2>
            <p>Please enter your credentials.</p>
            <input type="text" placeholder="Email">
            <input type="password" placeholder="Password">
            <button>Login</button>
        `;
    });

    document.getElementById("signupBtn").addEventListener("click", () => {
        content.innerHTML = `
            <h2>Sign Up</h2>
            <p>Create a new account.</p>
            <input type="text" placeholder="Full Name">
            <input type="email" placeholder="Email">
            <input type="password" placeholder="Password">
            <button>Register</button>
        `;
    });
});

// Payment Processing Function
function processPayment(amount) {
    let paymentMethod = prompt("Select Payment Method:\n1. Equity Bank\n2. I&M Bank\n3. Coop Bank\n4. KCB\n5. MPESA\n6. Binance");

    if (paymentMethod) {
        let pin = prompt("Enter Your Payment PIN:");

        if (pin === "1234") { // Placeholder for validation
            alert("Payment Successful! Order confirmed.");
        } else {
            alert("Transaction Failed. Returning to home.");
        }
    }
}
