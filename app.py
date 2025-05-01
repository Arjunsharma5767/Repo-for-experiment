<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hons Technology - Engineering Solutions</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #6a11cb;
            --secondary-color: #2575fc;
            --accent-color: #ffd166;
            --dark-color: #1a1a2e;
            --light-color: #f8f9fa;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            overflow-x: hidden;
        }
        
        /* Header and Navigation */
        .navbar {
            padding: 15px 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            background: linear-gradient(to right, rgba(106, 17, 203, 0.9), rgba(37, 117, 252, 0.9));
        }
        
        .navbar-brand {
            font-weight: 700;
            font-size: 1.8rem;
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        
        .nav-link {
            margin-right: 20px;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.9) !important;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            color: var(--accent-color) !important;
            transform: translateY(-2px);
        }
        
        .nav-button {
            background: linear-gradient(45deg, var(--accent-color), #ffb347);
            color: var(--dark-color);
            padding: 10px 25px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .nav-button:hover {
            background: linear-gradient(45deg, #ffb347, var(--accent-color));
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            color: var(--dark-color);
        }
        
        /* Hero Section */
        .hero {
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.9) 0%, rgba(37, 117, 252, 0.8) 100%), url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80') no-repeat fixed center center/cover;
            min-height: 600px;
            color: white;
            padding: 100px 0;
            text-align: center;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
            animation: pulse 8s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.3; }
            50% { transform: scale(1.5); opacity: 0.1; }
            100% { transform: scale(1); opacity: 0.3; }
        }
        
        .hero h1 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            position: relative;
            z-index: 2;
        }
        
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 40px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            position: relative;
            z-index: 2;
        }
        
        /* AI Button */
        .ai-button {
            background: linear-gradient(45deg, var(--accent-color), #ff9a3c);
            color: var(--dark-color);
            padding: 15px 40px;
            font-size: 1.3rem;
            border-radius: 50px;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
            margin-top: 30px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.25);
            position: relative;
            z-index: 2;
        }
        
        .ai-button:hover {
            background: linear-gradient(45deg, #ff9a3c, var(--accent-color));
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            color: var(--dark-color);
        }
        
        /* Section Styling */
        section {
            padding: 80px 0;
            position: relative;
            overflow: hidden;
        }
        
        section h2 {
            font-weight: 700;
            margin-bottom: 50px;
            position: relative;
            display: inline-block;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        section h2:after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 0;
            width: 60px;
            height: 4px;
            background: linear-gradient(to right, var(--accent-color), #ff9a3c);
        }
        
        .text-center h2:after {
            left: 50%;
            transform: translateX(-50%);
        }
        
        /* Service Cards */
        .service-card {
            border-radius: 15px;
            overflow: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            height: 100%;
            border: none;
        }
        
        .service-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }
        
        .service-img {
            height: 200px;
            object-fit: cover;
            transition: all 0.5s ease;
        }
        
        .service-card:hover .service-img {
            transform: scale(1.1);
        }
        
        .service-card .card-body {
            padding: 25px;
        }
        
        .service-card .card-title {
            font-weight: 600;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Project Section */
        .project-item {
            position: relative;
            overflow: hidden;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .project-img {
            transition: all 0.5s ease;
            width: 100%;
            height: 250px;
            object-fit: cover;
        }
        
        .project-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.9), rgba(37, 117, 252, 0.8));
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: all 0.5s ease;
        }
        
        .project-overlay-content {
            text-align: center;
            color: white;
            padding: 20px;
        }
        
        .project-overlay-content h4 {
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        .project-btn {
            background: var(--accent-color);
            color: var(--dark-color);
            padding: 10px 20px;
            border-radius: 30px;
            font-weight: 600;
            display: inline-block;
            margin-top: 15px;
            transition: all 0.3s ease;
        }
        
        .project-btn:hover {
            background: #ff9a3c;
            transform: translateY(-3px);
            color: var(--dark-color);
        }
        
        .project-item:hover .project-overlay {
            opacity: 1;
        }
        
        .project-item:hover .project-img {
            transform: scale(1.1);
        }
        
        /* Team Section */
        .team-member {
            text-align: center;
            margin-bottom: 30px;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .team-img-container {
            position: relative;
            width: 200px;
            height: 200px;
            margin: 0 auto 20px;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        }
        
        .team-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: all 0.5s ease;
        }
        
        .team-img:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.7), rgba(37, 117, 252, 0.7));
            opacity: 0;
            transition: all 0.5s ease;
        }
        
        .team-member:hover .team-img {
            transform: scale(1.1);
        }
        
        .team-member h4 {
            font-weight: 600;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .team-member p {
            color: #666;
            margin-bottom: 15px;
        }
        
        .social-icons a {
            display: inline-block;
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            border-radius: 50%;
            text-align: center;
            line-height: 36px;
            margin: 0 5px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        
        .social-icons a:hover {
            background: linear-gradient(135deg, var(--secondary-color), var(--primary-color));
            transform: translateY(-3px) rotate(10deg);
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        
        /* Testimonials */
        .testimonial {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 30px;
            position: relative;
            transition: all 0.3s ease;
        }
        
        .testimonial:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.12);
        }
        
        .testimonial:before {
            content: '\201C';
            font-size: 80px;
            position: absolute;
            top: -10px;
            left: 10px;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            opacity: 0.3;
        }
        
        .client-img {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            object-fit: cover;
            margin-right: 15px;
            border: 3px solid white;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .testimonial-rating {
            color: var(--accent-color);
            margin-bottom: 10px;
        }
        
        /* FAQ */
        .accordion-button:not(.collapsed) {
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.1), rgba(37, 117, 252, 0.1));
            color: var(--primary-color);
        }
        
        .accordion-button:focus {
            box-shadow: none;
            border-color: rgba(0,0,0,0.125);
        }
        
        .accordion-item {
            border-radius: 10px;
            margin-bottom: 15px;
            overflow: hidden;
            border: 1px solid rgba(0,0,0,0.1);
        }
        
        /* Contact */
        .contact-info {
            background: white;
            border-radius: 15px;
            padding: 35px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            height: 100%;
            transition: all 0.3s ease;
        }
        
        .contact-info:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.12);
        }
        
        .contact-info i {
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 28px;
            margin-bottom: 15px;
        }
        
        .contact-form {
            background: white;
            border-radius: 15px;
            padding: 35px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        }
        
        .form-control {
            padding: 12px 15px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        
        .form-control:focus {
            box-shadow: 0 0 0 3px rgba(106, 17, 203, 0.1);
            border-color: var(--primary-color);
        }
        
        .submit-btn {
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 12px 30px;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        
        .submit-btn:hover {
            background: linear-gradient(45deg, var(--secondary-color), var(--primary-color));
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        }
        
        /* Features */
        .feature-box {
            text-align: center;
            padding: 35px 25px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            margin-bottom: 30px;
            height: 100%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        
        .feature-box:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.05), rgba(37, 117, 252, 0.05));
            z-index: -1;
            opacity: 0;
            transition: all 0.5s ease;
        }
        
        .feature-box:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.12);
        }
        
        .feature-box:hover:before {
            opacity: 1;
        }
        
        .feature-icon {
            font-size: 44px;
            margin-bottom: 25px;
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Footer */
        footer {
            background: linear-gradient(135deg, var(--dark-color) 0%, #2c2c44 100%);
            color: white;
            padding: 60px 0 20px;
            position: relative;
        }
        
        footer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23ffffff' fill-opacity='0.03' fill-rule='evenodd'%3E%3Cpath d='M0 40L40 0H20L0 20M40 40V20L20 40'/%3E%3C/g%3E%3C/svg%3E");
            opacity: 0.15;
        }
        
        .footer-heading {
            font-weight: 600;
            margin-bottom: 25px;
            color: var(--accent-color);
        }
        
        .footer-link {
            display: block;
            color: rgba(255,255,255,0.7);
            margin-bottom: 12px;
            transition: all 0.3s ease;
        }
        
        .footer-link:hover {
            color: var(--accent-color);
            transform: translateX(5px);
            text-decoration: none;
        }
        
        .footer-bottom {
            padding-top: 40px;
            border-top: 1px solid rgba(255,255,255,0.1);
            margin-top: 40px;
            position: relative;
        }
        
        /* Newsletter */
        .newsletter-form {
            position: relative;
        }
        
        .newsletter-form .form-control {
            padding-right: 50px;
            background-color: rgba(255,255,255,0.1);
            border: none;
            color: white;
        }
        
        .newsletter-form .form-control::placeholder {
            color: rgba(255,255,255,0.5);
        }
        
        .newsletter-btn {
            position: absolute;
            top: 0;
            right: 0;
            height: 100%;
            width: 50px;
            background: linear-gradient(45deg, var(--accent-color), #ff9a3c);
            border: none;
            border-top-right-radius: 10px;
            border-bottom-right-radius: 10px;
            color: var(--dark-color);
            transition: all 0.3s ease;
        }
        
        .newsletter-btn:hover {
            background: linear-gradient(45deg, #ff9a3c, var(--accent-color));
        }
        
        /* Utilities */
        .bg-gradient-light {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        .bg-gradient-primary {
            background: linear-gradient(135deg, rgba(106, 17, 203, 0.1) 0%, rgba(37, 117, 252, 0.1) 100%);
        }
        
        .btn-outline-gradient {
            background: white;
            color: var(--primary-color);
            border: 2px solid transparent;
            background-clip: padding-box;
            position: relative;
        }
        
        .btn-outline-gradient:before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            z-index: -1;
            border-radius: 12px;
        }
        
        .text-gradient {
            background: linear-gradient(to right, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        
        .floating {
            animation: float 6s ease-in-out infinite;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#">
                <i class="fas fa-microchip me-2"></i>Hons Technology
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul class="navbar-nav align-items-center">
                    <li class="nav-item"><a class="nav-link" href="#home">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="#services">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="#products">Products</a></li>
                    <li class="nav-item"><a class="nav-link" href="#projects">Projects</a></li>
                    <li class="nav-item"><a class="nav-link" href="#team">Team</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Contact</a></li>
                    <li class="nav-item">
                        <a href="#contact" class="nav-button">Get Quote</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="mb-4">Engineering Excellence for the Digital Age</h1>
                    <p>Hons Technology delivers cutting-edge solutions in Electronics, Electrical Engineering, and Information Technology to transform your business and drive innovation.</p>
                    <a href="#ai-product" class="ai-button">
                        <i class="fas fa-brain me-2"></i>Explore AI Image Processing
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-5">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-4 mb-lg-0">
                    <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80" alt="About Hons Technology" class="img-fluid rounded-3 shadow">
                </div>
                <div class="col-lg-6">
                    <h2>About Hons Technology</h2>
                    <p class="lead">We are pioneers in integrated engineering solutions, bridging the gap between electronics, electrical systems, and information technology.</p>
                    <p>Founded in 2010, Hons Technology has grown from a small startup to a leading engineering firm with a global footprint. Our multidisciplinary team of engineers, technicians, and IT specialists work together to deliver comprehensive solutions that address complex challenges across industries.</p>
                    <p>We pride ourselves on our commitment to innovation, quality, and customer satisfaction. Our solutions are designed to be efficient, reliable, and future-proof, ensuring that our clients stay ahead in today's rapidly evolving technological landscape.</p>
                    <div class="row mt-4">
                        <div class="col-6">
                            <div class="d-flex align-items-center mb-3">
                                <i class="fas fa-check-circle text-gradient me-2"></i>
                                <span>15+ Years Experience</span>
                            </div>
                            <div class="d-flex align-items-center mb-3">
                                <i class="fas fa-check-circle text-gradient me-2"></i>
                                <span>500+ Projects Completed</span>
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="d-flex align-items-center mb-3">
                                <i class="fas fa-check-circle text-gradient me-2"></i>
                                <span>98% Client Satisfaction</span>
                            </div>
                            <div class="d-flex align-items-center mb-3">
                                <i class="fas fa-check-circle text-gradient me-2"></i>
                                <span>24/7 Technical Support</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="bg-gradient-light py-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-6 text-center">
                    <h2>Why Choose Hons Technology</h2>
                    <p class="mb-5">We combine technical expertise with industry knowledge to deliver solutions that create real business value.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-tools feature-icon"></i>
                        <h4>Comprehensive Expertise</h4>
                        <p>Our multidisciplinary team covers electronics, electrical engineering, and IT, providing integrated solutions under one roof.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-lightbulb feature-icon"></i>
                        <h4>Innovative Approach</h4>
                        <p>We stay at the forefront of technological advancements to deliver cutting-edge solutions that drive business growth.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-headset feature-icon"></i>
                        <h4>Dedicated Support</h4>
                        <p>Our customer support team is available 24/7 to address any issues and ensure smooth operation of your systems.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-shield-alt feature-icon"></i>
                        <h4>Quality Assurance</h4>
                        <p>Every solution undergoes rigorous testing to ensure reliability, performance, and longevity.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-cogs feature-icon"></i>
                        <h4>Customized Solutions</h4>
                        <p>We tailor our services to meet your specific needs, ensuring optimal performance and efficiency.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-box">
                        <i class="fas fa-chart-line feature-icon"></i>
                        <h4>Scalable Systems</h4>
                        <p>Our solutions are designed to grow with your business, adapting to changing needs and technologies.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section i
