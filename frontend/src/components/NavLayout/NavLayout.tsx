import Container from "react-bootstrap/Container";
import { Outlet, Link } from "react-router-dom";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import "./NavLayout.css";

const NavLayout = () => {
  return (
    <>
      <Navbar fixed="top" bg="transparent" variant="light">
        <Container className="nav-bar">
          <Navbar.Brand className="brand-title" as={Link} to="/">
            <i className="bi bi-robot"></i> NLProfessor
          </Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">
              Home
            </Nav.Link>
            <Nav.Link as={Link} to="/chat">
              Chat
            </Nav.Link>
            <Nav.Link as={Link} to="/recommendations">
              Recommendations
            </Nav.Link>
          </Nav>
          <Nav>
            <Nav.Link href="https://github.com/SonyaInSiberia/NLProfessor">
              <i className="bi bi-github"></i> GitHub
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <Outlet />
    </>
  );
};

export default NavLayout;
